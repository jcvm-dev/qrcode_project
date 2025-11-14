from fastapi import APIRouter, Response, Query, HTTPException
from starlette.responses import StreamingResponse
from io import BytesIO
import base64

from .schemas import QRCodeRequest
from .services.qrcode_service import generate_qrcode_image

router = APIRouter()

@router.post("/qrcode", tags=["QR Code"])
async def post_generate_qrcode(request: QRCodeRequest):
    try:
        image_bytes = await generate_qrcode_image(request)

        media_type = f"image/{request.format.lower().replace('jpg', 'jpeg')}"
        if request.format.lower() == "svg":
            media_type = "image/svg+xml"
        
        if request.mode and request.mode.lower() == "dataurl":
            encoded_image = base64.b64encode(image_bytes).decode("utf-8")
            data_url = f"data:{media_type};base64,{encoded_image}"
            return {"data_url": data_url}
        else:
            return Response(content=image_bytes, media_type=media_type)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar QR Code: {e}")

@router.get("/qrcode", tags=["QR Code"])
async def get_generate_qrcode(
    text: str = Query(..., description="O texto ou URL a ser codificado no QR Code."),
    size: int = Query(10, ge=1, le=40, description="Tamanho da caixa do QR Code (box_size)."),
    border: int = Query(4, ge=0, le=10, description="Espessura da borda do QR Code (border)."),
    format: str = Query("png", description="Formato da imagem de saída (png, jpeg, svg)."),
    fill_color: str = Query("#000000", description="Cor de preenchimento do QR Code (ex: #000000)."),
    back_color: str = Query("#FFFFFF", description="Cor de fundo do QR Code (ex: #FFFFFF)."),
):
    request_data = QRCodeRequest(
        text=text,
        size=size,
        border=border,
        format=format,
        fill_color=fill_color,
        back_color=back_color,
        mode=None
    )
    
    try:
        image_bytes = await generate_qrcode_image(request_data)

        media_type = f"image/{format.lower().replace('jpg', 'jpeg')}"
        if format.lower() == "svg":
            media_type = "image/svg+xml"

        return Response(content=image_bytes, media_type=media_type)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar QR Code: {e}")
