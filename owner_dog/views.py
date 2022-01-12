import json

from django.views import View
from django.http  import JsonResponse

from .models import Owner, Dog

class OwnerView(View):
    def get(self, request):
        """
        OUTPUT : {
            name : 철수,
            email : cheolsoo@email.com,
            age : 40,
            dogs : [
                {
                    name : 짱구,
                    age : 2
                }
            ]
        }
        """
        #GET 127.0.0.1:8000/owner
        owners = Owner.objects.all()
        results = []

        # for owner in owners:
        #     dogs = Dog.objects.filter(owner_id=owner.id)
        #     dogs_list = [{"name" : dog.name, "age" : dog.age} for dog in dogs]
        #     results.append(
        #         {           
        #             "name" : owner.name,
        #             "email" : owner.email,
        #             "age" : owner.age,
        #             "dogs" : dogs_list
        #         }
        #     )

        results.append(
            [{'id': owner.id, 'name' : owner.name, 'age' : owner.age, 'dogs' : {'name' : dog.name}, 'id' : dog.id} for owner in owners for dog in owner.dog_set.all()]
            )
            
        return JsonResponse({"owners" :results}, status=200) 


    def post(self, request):
        #POST 127.0.0.1:8000/owner
        """
        1. 목적 : 클라이언트로부터 받은 데이터를 데이터베이스에 등록하기 위함
        2. INPUT - 이름, 이메일, 나이
        {
            "name": "철수",
            "email": "cheolsoo@email.com",
            "age": 30
        }
        3. OUTPUT
        {
            "message" : "등록 성공"
        }
        """
        data = json.loads(request.body)
        
        owner = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )  
        

        return JsonResponse({"message" : "등록 성공"}, status=201)


class DogView(View):
    def get(self, request):
        """
        OUTPUT : {
            name : 짱구,
            age : 2,
            owner : {
                name : 철수,
                email : cheolsoo@email.com
            }
        }
        """
        #GET 127.0.0.1:8000/dog
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            owner = Owner.objects.get(id=dog.owner_id)
            owner_dict = {
                "name" : owner.name,
                "email" : owner.email
            } 
            owner_name = owner.name
            results.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : owner_dict
                }
            )

        return JsonResponse({"dogs" :results}, status=200) 


    def post(self, request):
        #POST 127.0.0.1:8000/dog
        """
        1. 목적 : 클라이언트로부터 받은 데이터를 데이터베이스에 등록하기 위함
        2. INPUT - 보호자 id, 이름, 나이
        {
            "owner_id": 1,
            "name": "바둑이",
            "age": 2
        }
        3. OUTPUT
        {
            "message" : "등록 성공"
        }
        """
        data = json.loads(request.body)
        
        dog = Dog.objects.create(
            owner_id = data['owner_id'],
            name = data['name'],
            age = data['age']    
        )

        return JsonResponse({"message" : "등록 성공"}, status=201)