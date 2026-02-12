from .products import router as prod_router
from .categories import router as cat_router
from .cart import router as cart_router


__all__ = ["prod_router", "cat_router", "cart_router"]