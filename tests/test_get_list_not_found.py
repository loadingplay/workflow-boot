import unittest
import json
from unittest.mock import patch
from app.get_list_not_found import GetDocumentsNotFound


class GetDocumentsNotFoundTestCase(unittest.TestCase):
    @patch("app.get_list_not_found.requests.get")
    def test_get_orders(self, mock_get_orders):
        input_data = {
            "token": "token-test",
            "date_min": "2022-01-1",
            "date_max": "2022-01-2"
        }
        token = "token-test",
        date_min = "2022-01-1",
        date_max = "2022-01-2",

        return_mock_get_orders = {
            "status": "success",
            "orders": [
                {
                    "id": 625970,
                    "date": "2022-09-21T14:58:09.953674",
                    "type": 1,
                    "subtotal": 2000.0,
                    "shipping": 0.0,
                    "tax": 0.0,
                    "total": 2000.0,
                    "items_quantity": "None",
                    "products_quantity": "None",
                    "billing_id": 26646766,
                    "shipping_id": 26646766,
                    "payment_type": "shopify",
                    "source": "",
                    "voucher": "",
                    "tracking_code": "",
                    "provider_id": "None",
                    "site_id": "None",
                    "extra_info": "{\"name\": \"#1086\", \"bill_comment\": \"Pedido Shopify: #1086\", \"payment_gateway\": [\"Pago mensual via transferencia\"], \"checkout_id\": 22069108506684, \"processing_method\": \"manual\", \"currency\": \"CLP\", \"mail_info\": {\"customer_mail\": false, \"bcc_mail\": {\"status\": \"sent\", \"reject_reason\": null, \"timestamp\": \"2022-06-14T20:37:38.519478\", \"mail\": \"all@loadingplay.com\"}}, \"bsale_nota_venta\": {\"id\": 47046, \"url\": \"https://app2.bsale.cl/view/17927/4a9c7c30de51.pdf?sfd=99\", \"expiration_date\": 1627430400, \"emission_date\": 1627430400, \"generation_date\": 1627481509, \"folio\": 2384, \"document_type_id\": \"42\", \"document_name\": \"NOTA VENTA\", \"office_id\": \"1\", \"cancelled\": false}, \"document_generation_skipped_reason\": \"Document Stock Reserve already exist\"}",
                    "name": "",
                    "reference_code": "",
                    "adjustment": 0.0,
                    "origin": "shopify",
                    "url_document": "",
                    "site_name": "workflows",
                    "status": "por confirmar",
                    "discount_code": "",
                    "customer_id": 2794571,
                    "cellar_id": 720,
                    "status_counter": 0,
                    "tags": "",
                    "payments": [
                    ]
                },
                {
                    "id": 625969,
                    "date": "2022-09-21T14:57:58.854587",
                    "type": 1,
                    "subtotal": 2000.0,
                    "shipping": 0.0,
                    "tax": 0.0,
                    "total": 2000.0,
                    "items_quantity": "None",
                    "products_quantity": "None",
                    "billing_id": 26646765,
                    "shipping_id": 26646765,
                    "payment_type": "shopify",
                    "source": "",
                    "voucher": "",
                    "tracking_code": "",
                    "provider_id": "None",
                    "site_id": "None",
                    "extra_info": "{\"name\": \"#1086\", \"bill_comment\": \"Pedido Shopify: #1086\", \"payment_gateway\": [\"Pago mensual via transferencia\"], \"checkout_id\": 22069108506684, \"processing_method\": \"manual\", \"currency\": \"CLP\", \"mail_info\": {\"customer_mail\": false, \"bcc_mail\": {\"status\": \"sent\", \"reject_reason\": null, \"timestamp\": \"2022-06-14T20:37:38.519478\", \"mail\": \"all@loadingplay.com\"}}, \"bsale_nota_venta\": {\"id\": 47046, \"url\": \"https://app2.bsale.cl/view/17927/4a9c7c30de51.pdf?sfd=99\", \"expiration_date\": 1627430400, \"emission_date\": 1627430400, \"generation_date\": 1627481509, \"folio\": 2384, \"document_type_id\": \"42\", \"document_name\": \"NOTA VENTA\", \"office_id\": \"1\", \"cancelled\": false}, \"document_generation_skipped_reason\": \"Document Stock Reserve already exist\"}",
                    "name": "",
                    "reference_code": "",
                    "adjustment": 0.0,
                    "origin": "shopify",
                    "url_document": "",
                    "site_name": "workflows",
                    "status": "por confirmar",
                    "discount_code": "",
                    "customer_id": 2794570,
                    "cellar_id": 720,
                    "status_counter": 0,
                    "tags": "",
                    "payments": [
                    ]
                }
            ]
        }

        expected_ouput = return_mock_get_orders

        mock_get_orders.return_value.json.return_value = return_mock_get_orders

        send_data = GetDocumentsNotFound(input_data)
        result = send_data.get_orders(token, date_min, date_max)
        assert result == expected_ouput

    def test_filter_orders_without_invoice(self):
        input_data = [
            {
                "id":625970,
                "date":"2022-09-21T14:58:09.953674",
                "type":1,
                "subtotal":2000.0,
                "shipping":0.0,
                "tax":0.0,
                "total":2000.0,
                "items_quantity":"None",
                "products_quantity":"None",
                "billing_id":26646766,
                "shipping_id":26646766,
                "payment_type":"shopify",
                "source":"",
                "voucher":"",
                "tracking_code":"",
                "provider_id":"None",
                "site_id":"None",
                "extra_info":"{\"name\": \"#1086\", \"bill_comment\": \"Pedido Shopify: #1086\", \"payment_gateway\": [\"Pago mensual via transferencia\"], \"checkout_id\": 22069108506684, \"processing_method\": \"manual\", \"currency\": \"CLP\", \"mail_info\": {\"customer_mail\": false, \"bcc_mail\": {\"status\": \"sent\", \"reject_reason\": null, \"timestamp\": \"2022-06-14T20:37:38.519478\", \"mail\": \"all@loadingplay.com\"}}, \"bsale_nota_venta\": {\"id\": 47046, \"url\": \"https://app2.bsale.cl/view/17927/4a9c7c30de51.pdf?sfd=99\", \"expiration_date\": 1627430400, \"emission_date\": 1627430400, \"generation_date\": 1627481509, \"folio\": 2384, \"document_type_id\": \"42\", \"document_name\": \"NOTA VENTA\", \"office_id\": \"1\", \"cancelled\": false}, \"document_generation_skipped_reason\": \"Document Stock Reserve already exist\"}",
                "name":"",
                "reference_code":"",
                "adjustment":0.0,
                "origin":"shopify",
                "url_document":"",
                "site_name":"workflows",
                "status":"por confirmar",
                "discount_code":"",
                "customer_id":2794571,
                "cellar_id":720,
                "status_counter":0,
                "tags":"",
                "payments":[
                ]
            },
            {
                "id":625969,
                "date":"2022-09-21T14:57:58.854587",
                "type":1,
                "subtotal":2000.0,
                "shipping":0.0,
                "tax":0.0,
                "total":2000.0,
                "items_quantity":"None",
                "products_quantity":"None",
                "billing_id":26646765,
                "shipping_id":26646765,
                "payment_type":"shopify",
                "source":"",
                "voucher":"",
                "tracking_code":"",
                "provider_id":"None",
                "site_id":"None",
                "extra_info":"{\"name\": \"#1086\", \"bill_comment\": \"Pedido Shopify: #1086\", \"payment_gateway\": [\"Pago mensual via transferencia\"], \"checkout_id\": 22069108506684, \"processing_method\": \"manual\", \"currency\": \"CLP\", \"mail_info\": {\"customer_mail\": false, \"bcc_mail\": {\"status\": \"sent\", \"reject_reason\": null, \"timestamp\": \"2022-06-14T20:37:38.519478\", \"mail\": \"all@loadingplay.com\"}}, \"bsale_nota_venta\": {\"id\": 47046, \"url\": \"https://app2.bsale.cl/view/17927/4a9c7c30de51.pdf?sfd=99\", \"expiration_date\": 1627430400, \"emission_date\": 1627430400, \"generation_date\": 1627481509, \"folio\": 2384, \"document_type_id\": \"42\", \"document_name\": \"NOTA VENTA\", \"office_id\": \"1\", \"cancelled\": false}, \"document_generation_skipped_reason\": \"Document Stock Reserve already exist\"}",
                "name":"",
                "reference_code":"",
                "adjustment":0.0,
                "origin":"shopify",
                "url_document":"",
                "site_name":"workflows",
                "status":"por confirmar",
                "discount_code":"",
                "customer_id":2794570,
                "cellar_id":720,
                "status_counter":0,
                "tags":"",
                "payments":[
                ]
            }
        ]

        expected_ouput = [
            {
                "id":625970,
                "date":"2022-09-21T14:58:09.953674",
                "type":1,
                "subtotal":2000.0,
                "shipping":0.0,
                "tax":0.0,
                "total":2000.0,
                "items_quantity":"None",
                "products_quantity":"None",
                "billing_id":26646766,
                "shipping_id":26646766,
                "payment_type":"shopify",
                "source":"",
                "voucher":"",
                "tracking_code":"",
                "provider_id":"None",
                "site_id":"None",
                "extra_info":"{\"name\": \"#1086\", \"bill_comment\": \"Pedido Shopify: #1086\", \"payment_gateway\": [\"Pago mensual via transferencia\"], \"checkout_id\": 22069108506684, \"processing_method\": \"manual\", \"currency\": \"CLP\", \"mail_info\": {\"customer_mail\": false, \"bcc_mail\": {\"status\": \"sent\", \"reject_reason\": null, \"timestamp\": \"2022-06-14T20:37:38.519478\", \"mail\": \"all@loadingplay.com\"}}, \"bsale_nota_venta\": {\"id\": 47046, \"url\": \"https://app2.bsale.cl/view/17927/4a9c7c30de51.pdf?sfd=99\", \"expiration_date\": 1627430400, \"emission_date\": 1627430400, \"generation_date\": 1627481509, \"folio\": 2384, \"document_type_id\": \"42\", \"document_name\": \"NOTA VENTA\", \"office_id\": \"1\", \"cancelled\": false}, \"document_generation_skipped_reason\": \"Document Stock Reserve already exist\"}",
                "name":"",
                "reference_code":"",
                "adjustment":0.0,
                "origin":"shopify",
                "url_document":"",
                "site_name":"workflows",
                "status":"por confirmar",
                "discount_code":"",
                "customer_id":2794571,
                "cellar_id":720,
                "status_counter":0,
                "tags":"",
                "payments":[
                ]
            },
            {
                "id":625969,
                "date":"2022-09-21T14:57:58.854587",
                "type":1,
                "subtotal":2000.0,
                "shipping":0.0,
                "tax":0.0,
                "total":2000.0,
                "items_quantity":"None",
                "products_quantity":"None",
                "billing_id":26646765,
                "shipping_id":26646765,
                "payment_type":"shopify",
                "source":"",
                "voucher":"",
                "tracking_code":"",
                "provider_id":"None",
                "site_id":"None",
                "extra_info":"{\"name\": \"#1086\", \"bill_comment\": \"Pedido Shopify: #1086\", \"payment_gateway\": [\"Pago mensual via transferencia\"], \"checkout_id\": 22069108506684, \"processing_method\": \"manual\", \"currency\": \"CLP\", \"mail_info\": {\"customer_mail\": false, \"bcc_mail\": {\"status\": \"sent\", \"reject_reason\": null, \"timestamp\": \"2022-06-14T20:37:38.519478\", \"mail\": \"all@loadingplay.com\"}}, \"bsale_nota_venta\": {\"id\": 47046, \"url\": \"https://app2.bsale.cl/view/17927/4a9c7c30de51.pdf?sfd=99\", \"expiration_date\": 1627430400, \"emission_date\": 1627430400, \"generation_date\": 1627481509, \"folio\": 2384, \"document_type_id\": \"42\", \"document_name\": \"NOTA VENTA\", \"office_id\": \"1\", \"cancelled\": false}, \"document_generation_skipped_reason\": \"Document Stock Reserve already exist\"}",
                "name":"",
                "reference_code":"",
                "adjustment":0.0,
                "origin":"shopify",
                "url_document":"",
                "site_name":"workflows",
                "status":"por confirmar",
                "discount_code":"",
                "customer_id":2794570,
                "cellar_id":720,
                "status_counter":0,
                "tags":"",
                "payments":[
                ]
            }
        ]


        send_data = GetDocumentsNotFound("")
        result = send_data.filter_orders_without_invoice(input_data)
        assert result == expected_ouput


    @patch("app.get_list_not_found.requests.get")
    def test_transform_orders(self, mock_get):
        token = "token-test",
        order_json = {
            "id":625970,
            "date":"2022-09-21T14:58:09.953674",
            "type":1,
            "subtotal":2000.0,
            "shipping":0.0,
            "tax":0.0,
            "total":2000.0,
            "items_quantity":"None",
            "products_quantity":"None",
            "billing_id":26646766,
            "shipping_id":26646766,
            "payment_type":"shopify",
            "source":"",
            "voucher":"",
            "tracking_code":"",
            "provider_id":"None",
            "site_id":"None",
            "extra_info":"{\"name\": \"#1086\", \"bill_comment\": \"Pedido Shopify: #1086\", \"payment_gateway\": [\"Pago mensual via transferencia\"], \"checkout_id\": 22069108506684, \"processing_method\": \"manual\", \"currency\": \"CLP\", \"mail_info\": {\"customer_mail\": false, \"bcc_mail\": {\"status\": \"sent\", \"reject_reason\": null, \"timestamp\": \"2022-06-14T20:37:38.519478\", \"mail\": \"all@loadingplay.com\"}}, \"bsale_nota_venta\": {\"id\": 47046, \"url\": \"https://app2.bsale.cl/view/17927/4a9c7c30de51.pdf?sfd=99\", \"expiration_date\": 1627430400, \"emission_date\": 1627430400, \"generation_date\": 1627481509, \"folio\": 2384, \"document_type_id\": \"42\", \"document_name\": \"NOTA VENTA\", \"office_id\": \"1\", \"cancelled\": false}, \"document_generation_skipped_reason\": \"Document Stock Reserve already exist\"}",
            "name":"",
            "reference_code":"",
            "adjustment":0.0,
            "origin":"shopify",
            "url_document":"",
            "site_name":"workflows",
            "status":"por confirmar",
            "discount_code":"",
            "customer_id":2794571,
            "cellar_id":720,
            "status_counter":0,
            "tags":"",
            "payments":[
            ]
        }

        return_mock_get_product = {
            "status":"success",
            "products":[
                {
                    "id":1219683,
                    "quantity":1.0,
                    "subtotal":2000.0,
                    "order_id":625901,
                    "size":"",
                    "price":2000.0,
                    "combination":"",
                    "sku":"1000",
                    "name":"Conecta Bsale & Multivende",
                    "discount":0.0,
                    "barcode":"",
                    "cellar_id":"2402"
                }
            ]
        }
        return_mock_get_contact = {
            "status":"success",
            "contact":{
                "success":[
                    {
                        "id":26646695,
                        "name":"",
                        "email":"",
                        "address":"",
                        "telephone":"",
                        "zip_code":"",
                        "additional_info":"",
                        "town":"",
                        "country":"chile",
                        "rut":"",
                        "type":"persona",
                        "city":"",
                        "region":"",
                        "customer_id":2794500,
                        "last_name":""
                    }
                ]
            }
        }
        return_mock_get_customer = {
            "status":"success",
            "contact":{
                "success":[
                    {
                        "id":26646695,
                        "name":"",
                        "email":"",
                        "address":"",
                        "telephone":"",
                        "zip_code":"",
                        "additional_info":"",
                        "town":"",
                        "country":"chile",
                        "rut":"",
                        "type":"persona",
                        "city":"",
                        "region":"",
                        "customer_id":2794500,
                        "last_name":""
                    }
                ]
            }
        }

        expected_ouput = {
            'id': 625970,
            'date': '2022-09-21T14:58:09.953674',
            'type': 1,
            'subtotal': 2000.0,
            'shipping': {
                'cost': 0.0,
                'address_line_1': '',
                'address_line_2': '',
                'city': '',
                'town': '',
                'country': 'chile'},
                'tax': 0.0,
                'total': 2000.0,
                'items_quantity': 'None',
                'products_quantity': 'None',
                'billing_id': 26646766,
                'shipping_id': 26646766,
                'payment_type': 'shopify',
                'source': '',
                'voucher': '',
                'tracking_code': '',
                'provider_id': 'None',
                'site_id': 'None',
                'extra_info': {
                    'name': '#1086',
                    'bill_comment': 'Pedido Shopify: #1086',
                    'payment_gateway': [
                        'Pago mensual via transferencia'
                        ],
                        'checkout_id': 22069108506684,
                        'processing_method': 'manual',
                        'currency': 'CLP',
                        'mail_info': {
                            'customer_mail': False,
                            'bcc_mail': {
                                'status': 'sent',
                                'reject_reason': None,
                                'timestamp': '2022-06-14T20:37:38.519478',
                                'mail': 'all@loadingplay.com'
                            }
                        },
                        'bsale_nota_venta': {
                            'id': 47046,
                            'url': 'https://app2.bsale.cl/view/17927/4a9c7c30de51.pdf?sfd=99',
                            'expiration_date': 1627430400,
                            'emission_date': 1627430400,
                            'generation_date': 1627481509,
                            'folio': 2384,
                            'document_type_id': '42',
                            'document_name': 'NOTA VENTA',
                            'office_id': '1',
                            'cancelled': False
                        },
                        'document_generation_skipped_reason': 'Document Stock Reserve already exist'
                    },
                    'name': '',
                    'reference_code': '',
                    'adjustment': 0.0,
                    'origin': 'shopify',
                    'url_document': '',
                    'site_name': 'workflows',
                    'status': 'confirmado',
                    'discount_code': '',
                    'customer_id': 2794571,
                    'cellar_id': 720,
                    'status_counter': 0,
                    'tags': '',
                    'payments': [],
                    'products': [
                        {
                            'id': 1219683,
                            'quantity': 1.0,
                            'subtotal': 2000.0,
                            'order_id': 625901,
                            'size': '',
                            'price': 2000.0,
                            'combination': '',
                            'sku': '1000',
                            'name': 'Conecta Bsale & Multivende',
                            'discount': 0.0,
                            'barcode': '',
                            'cellar_id': '2402'
                        }
                    ], 
                    'customer': {
                        'id': 26646695,
                        'name': '',
                        'email': '',
                        'address': '',
                        'telephone': '',
                        'zip_code': '',
                        'additional_info': '',
                        'town': '',
                        'country': 'chile',
                        'rut': '',
                        'type': 'persona',
                        'city': '',
                        'region': '',
                        'customer_id': 2794500,
                        'last_name': ''
                    }
                }
        mock_get.return_value.json.side_effect = [return_mock_get_product, return_mock_get_contact, return_mock_get_customer]

        send_data = GetDocumentsNotFound("")
        result = send_data.transform_orders(token, order_json)
        self.assertEqual(result, expected_ouput)
