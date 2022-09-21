import requests
from fastapi import HTTPException
import logging
import json
import os
import base64

# logging.getLogger().setLevel(logging.INFO)

# LP_API = os.getenv('LP_API', '')
LP_API = "https://apibodegas.ondev.today"


class GetDocumentsNotFound():
    def __init__(self, data) -> None:
        self.__data = data

    def get_orders(self, token, date_min="", date_max=""):
        url = f"{LP_API}/v1/order"

        params = {
            "dateMin": date_min,
            "dateMax": date_max,
            "items": 4000
        }

        headers = {
            "Authorization": f"Bearer {token}",
        }

        response = requests.get(url, headers=headers, params=params)

        return response.json()

    def filter_orders_without_invoice(self, collected_orders):
        orders_without_invoice = []
        #print(collected_orders)
        for order in collected_orders:
            if not order["url_document"]:
                orders_without_invoice.append(order)

        return orders_without_invoice

    def encode_orders_to_send(self, token, workflow_id, orders_without_invoice):
        encoded_orders = []
        for order in orders_without_invoice:
            transformed_order = self.transform_orders(token, order)
            json_data = {
                "order": transformed_order,
                "workflow": workflow_id
            }
            encoded_order = self.order_to_base64(json_data)
            encoded_orders.append(encoded_order)

        return encoded_orders

    def order_to_base64(self, json_data):
        return base64.b64encode(
            json.dumps(
                json_data).encode("ascii")).decode("ascii")

    def transform_orders(self, token, order_json, override_customer_dni=""):
        # get order detail
        order_id = order_json["id"]
        resp = requests.get(
            f"{LP_API}/v1/order/{order_id}/detail",
            headers={"Authorization": "Bearer " + token}
        )

        order_json["products"] = resp.json()["products"]

        # TODO: fix this once API is fixed
        # get shipping
        shipping_cost = order_json["shipping"]
        resp = requests.get(
            f"{LP_API}/v1/contact/" +
            str(order_json["customer_id"]),
            headers={"Authorization": "Bearer " + token}
        )

        contacts = resp.json()["contact"]["success"]
        for c in contacts:
            if c["id"] == order_json["billing_id"]:
                order_json["shipping"] = {
                    "cost": shipping_cost,
                    "address_line_1": c["address"],
                    "address_line_2": c["additional_info"],
                    "city": c["region"],
                    "town": c["city"],
                    "country": c["country"]
                }

            if c == contacts[-1] and type(order_json["shipping"]) is not dict:
                order_json["shipping"] = {
                    "cost": shipping_cost,
                    "address_line_1": c["address"],
                    "address_line_2": c["additional_info"],
                    "city": c["region"],
                    "town": c["city"],
                    "country": c["country"]
                }

        # get customer
        resp = requests.get(
            str(LP_API) + "/v1/contact/" +
            str(order_json["customer_id"]),
            headers={"Authorization": "Bearer " + token}
        )

        contact = resp.json()["contact"]["success"][0]
        order_json["customer"] = contact

        # extra_info
        order_json["extra_info"] = json.loads(
            order_json["extra_info"].replace("\n", "\\n"))

        # allow to override some fields
        if override_customer_dni != "":
            order_json["customer"]["rut"] = override_customer_dni

        order_json["status"] = "confirmado"

        return order_json

    def send_run_workflow(self, encoded_action):
        url = "https://workflows-mcbra3u5lq-uc.a.run.app/v1/workflow/run"
        body = {
            "message": {
                "attributes": [],
                "data": encoded_action
            },
            "subscription": ""
        }
        response = requests.post(url, json=body)
        return response.json()

    def get_order(self, token, order_id):
        url = f"{LP_API}/v1/order/{order_id}"

        headers = {
            "Authorization": f"Bearer {token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_documents(self):
        token = self.__data["token"]
        date_min = self.__data["date_min"]
        date_max = self.__data["date_max"]
        order_failled = {}

        generate_orders_in_proccess = True

        collected_orders = self.get_orders(token, date_min, date_max)["orders"]

        orders_without_invoice = self.filter_orders_without_invoice(
            collected_orders
        )

        print("ordenes sin boleta:", len(orders_without_invoice))

        orders_without_invoice.reverse()
        if not generate_orders_in_proccess:
            encoded_orders = self.encode_orders_to_send(
                token,
                orders_without_invoice
            )
            for order in encoded_orders:
                print(self.send_run_workflow(order))
        # verificar que se genero la boleta
        count = 0
        for order in orders_without_invoice:
            order_collected = self.get_order(token, order["id"])["order"]
            extra_colection = json.loads(order_collected["extra_info"])
            if not order_collected["url_document"] and not extra_colection.get("bsale_nota_venta", ""):
                count = count + 1
                order_with_error = extra_colection.get(
                    "name", "") + " - " + extra_colection.get(
                    "document_generation_error", "")
                order_failled[order["id"]] = order_with_error

        return {
            "order_not_found": count,
            "order": order_failled}
