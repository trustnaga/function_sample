import logging
import json
import azure.functions as func
import azure.durable_functions as df
from pure_python_package import Person

myApp = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@myApp.route(route="query")
@myApp.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    Person().say_hello()
    result = json.dumps({
            'topic': "topic" ,
            'answer': "answer",       
            'question': "question"
                  
        })
    return func.HttpResponse(result, mimetype="application/json") 



