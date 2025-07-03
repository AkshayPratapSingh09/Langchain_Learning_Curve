from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str = 'akshay'   #-> akshay is set as default value
    age: Optional[int] = None
    email:EmailStr
    cgpa:float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')

new_student = {'age':"32",'email':'abc@gmail.com'}

student = Student(**new_student)
print(student)
print(type(student))
