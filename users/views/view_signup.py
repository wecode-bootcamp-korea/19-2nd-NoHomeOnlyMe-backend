import json
import bcrypt

from django.db            import IntegrityError
from django.http.response import (HttpResponse, HttpResponseBadRequest)
from django.views         import View

from users.utils  import validate_data
from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            validated_data = validate_data(**data)
            if type(validated_data) == str:
                return HttpResponseBadRequest(validated_data)
            validated_data["password"] = bcrypt.hashpw(validated_data["password"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            User.objects.create(**validated_data)
            
            return HttpResponse(f"{data['email']} Created Successful", status = 201)
        
        except IntegrityError:
            return HttpResponseBadRequest(f"{data['email']} already exists")