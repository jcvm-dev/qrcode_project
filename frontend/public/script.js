const API_BASE_URL = "/api/qrcode";

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('qrcode-form');
    const qrcodeImage = document.getElementById('qrcode-image');
    const downloadButton = document.getElementById('download-button');
    const loadingMessage = document.getElementById('loading-message');
    const errorMessage = document.getElementById('error-message');

    let lastGeneratedDataUrl = null;

    const toggleElements = (loading, error, image, download) => {
        loadingMessage.style.display = loading ? 'block' : 'none';
        errorMessage.style.display = error ? 'block' : 'none';
        qrcodeImage.style.display = image ? 'block' : 'none';
        downloadButton.style.display = download ? 'block' : 'none';
    };

    const generateQRCode = async (event) => {
        event.preventDefault();
        toggleElements(true, false, false, false);
        errorMessage.textContent = '';

        const formData = new FormData(form);
        const data = {
            text: formData.get('text'),
            size: parseInt(formData.get('size')),
            border: parseInt(formData.get('border')),
            format: formData.get('format'),
            fill_color: formData.get('fill_color'),
            back_color: formData.get('back_color'),
            mode: 'dataurl'
        };

        try {
            const url = API_BASE_URL; 

            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                let errorDetail = `Erro HTTP: ${response.status}`;
                try {
                    const errorData = await response.json();
                    errorDetail = errorData.detail || errorDetail;
                } catch (e) {}
                throw new Error(errorDetail);
            }

            const result = await response.json();
            lastGeneratedDataUrl = result.data_url;
            
            qrcodeImage.src = lastGeneratedDataUrl;
            toggleElements(false, false, true, true);

        } catch (error) {
            console.error('Erro ao gerar QR Code:', error);
            errorMessage.textContent = `Falha ao gerar QR Code: ${error.message}`;
            toggleElements(false, true, false, false);
        }
    };

    const downloadQRCode = () => {
        if (!lastGeneratedDataUrl) return;

        const link = document.createElement('a');
        link.href = lastGeneratedDataUrl;
        
        const format = document.getElementById('format').value;
        const text = document.getElementById('text').value.substring(0, 20).replace(/[^a-z0-9]/gi, '_');
        
        link.download = `qrcode_${text}.${format}`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    form.addEventListener('submit', generateQRCode);
    downloadButton.addEventListener('click', downloadQRCode);

    form.dispatchEvent(new Event('submit'));
});
