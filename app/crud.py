from sqlalchemy.orm import Session

from . import models, schemas


# -------------------------
# USER CRUD
# -------------------------

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


# -------------------------
# PRODUCT CRUD
# -------------------------

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()


def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)

    if product:
        db.delete(product)
        db.commit()

    return product


# -------------------------
# ORDER CRUD
# -------------------------

def create_order(db: Session, order: schemas.OrderCreate):
    product = get_product(db, order.product_id)

    if not product:
        return None

    if product.stock < order.quantity:
        return None

    product.stock -= order.quantity

    db_order = models.Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order


def get_orders(db: Session):
    return db.query(models.Order).all()


def get_user_orders(db: Session, user_id: int):
    return db.query(models.Order).filter(
        models.Order.user_id == user_id
    ).all()