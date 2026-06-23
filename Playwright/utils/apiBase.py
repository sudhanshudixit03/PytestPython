from multiprocessing.context import AuthenticationError

from playwright.sync_api import Playwright
ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
loginPayload = {"userEmail":"sudhanshudixit078@gmail.com","userPassword":"Sud@1234"}


class APIUtils:

    def getToken(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",data=loginPayload)
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/order/create-order",
                                 data = ordersPayload,headers={"Authentication":token,
                                                                "content-type":"application/json"
                                                                })
        print(response.json())