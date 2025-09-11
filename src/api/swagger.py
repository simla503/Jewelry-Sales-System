from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from src.api.schemas.todo import TodoRequestSchema, TodoResponseSchema
from src.api.schemas.user import RegisterRequestSchema, LoginRequestSchema, UserResponseSchema

spec = APISpec(
    title="Jewelry Sales System API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)

# Đăng ký schemas
spec.components.schema("TodoRequest", schema=TodoRequestSchema)
spec.components.schema("TodoResponse", schema=TodoResponseSchema)

spec.components.schema("RegisterRequest", schema=RegisterRequestSchema)
spec.components.schema("LoginRequest", schema=LoginRequestSchema)
spec.components.schema("UserResponse", schema=UserResponseSchema)
