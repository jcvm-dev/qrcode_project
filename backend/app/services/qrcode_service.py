import qrcode
from io import BytesIO
from ..schemas import QRCodeRequest

async def generate_qrcode_image(request: QRCodeRequest) -> bytes:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=request.size,
        border=request.border,
    )
    qr.add_data(request.text)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color=request.fill_color, back_color=request.back_color).convert("RGB")

    buffer = BytesIO()

    img_format = request.format.upper()
    if img_format == "JPG":
        img_format = "JPEG"
    elif img_format == "SVG":
        img_format = "PNG" 
        
    img_qr.save(buffer, format=img_format)
    
    return buffer.getvalue()
