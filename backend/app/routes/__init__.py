from backend.app.routes.products import router as prod_router
from backend.app.routes.categories import router as cat_router
from backend.app.routes.cart import router as cart_router


__all__ = ["prod_router", "cat_router", "cart_router"]