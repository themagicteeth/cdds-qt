# -*- coding: utf-8 -*-

"""Functions for generating content data"""


def generate_uuid():
    """Generates a random 16 digit UUID"""
    from uuid import uuid4
    new_uuid = uuid4()
    return str(new_uuid)


def generate_sku():
    """Generates a random seven digit product SKU"""
    from random import randint
    sku = randint(1000000, 9999999)
    return sku


def generate_dim_name(file_name):
    """Strips the extension and spaces from an uploaded file"""
    return file_name.rsplit('/', 1)[-1].split(".", 1)[0]
    # .replace(" ", "")


def write_supplement(product_name):
    """Creates the Supplement.dsx"""
    from string import Template

    supplement_template = Template('''
<ProductSupplement VERSION="0.1">
    <ProductName VALUE="$product"/>
    <InstallTypes VALUE="Content"/>
    <ProductTags VALUE="DAZStudio4_5"/>
</ProductSupplement>
''')

    return supplement_template.substitute(product=product_name)
