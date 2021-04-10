import uuid

def generate_code():
    code = uuid.uuid4()
    code = str(code).replace('-', '')[:12].upper()
    return code