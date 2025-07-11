# gateway/gateway.py
from flask import Blueprint, jsonify, request
from services.auth_service import auth_bp
from services.product_service import product_bp
from services.user_service import user_bp

gateway_bp = Blueprint('gateway', __name__, url_prefix='/api')

# Đăng ký các blueprint
gateway_bp.register_blueprint(auth_bp, url_prefix='/auth')       # → /api/auth
gateway_bp.register_blueprint(product_bp)                        # → /api/products (vì product_bp đã có prefix)
gateway_bp.register_blueprint(user_bp, url_prefix='/users')      # → /api/users

@gateway_bp.route('/')
def api_root():
    return jsonify({"message": "Welcome to the API Gateway"})

@gateway_bp.before_request
def log_gateway():
    print(f"[Gateway] Request path: {request.path}")
