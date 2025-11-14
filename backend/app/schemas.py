from pydantic import BaseModel, Field
from typing import Optional

class QRCodeRequest(BaseModel):
    text: str = Field(..., description="O texto ou URL a ser codificado no QR Code.")
    size: int = Field(10, ge=1, le=40, description="Tamanho da caixa do QR Code (box_size).")
    border: int = Field(4, ge=0, le=10, description="Espessura da borda do QR Code (border).")
    format: str = Field("png", description="Formato da imagem de saída (png, jpeg, svg).")
    fill_color: str = Field("#000000", description="Cor de preenchimento do QR Code (ex: #000000 ou black).")
    back_color: str = Field("#FFFFFF", description="Cor de fundo do QR Code (ex: #FFFFFF ou white).")
    mode: Optional[str] = Field(None, description="Se 'dataurl', retorna a imagem como data URL base64.")
