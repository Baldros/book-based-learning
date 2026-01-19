from urllib.request import urlopen
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io

def get_image(url, titulo=None, tamanho_figura=None):
    """
    Baixa e exibe uma imagem a partir de uma URL.
    
    Parâmetros:
    -----------
    url : str
        URL da imagem a ser baixada e exibida
    titulo : str, opcional
        Título a ser exibido acima da imagem
    tamanho_figura : tuple, opcional
        Tamanho da figura no formato (largura, altura) em polegadas
    
    Exemplo:
    --------
    >>> mostrar_imagem_url("https://example.com/imagem.png")
    >>> mostrar_imagem_url("https://example.com/imagem.png", titulo="Minha Imagem", tamanho_figura=(10, 8))
    """
    try:
        with urlopen(url) as response:
            image_data = response.read()
        
        img = mpimg.imread(io.BytesIO(image_data), format='png')
        
        if tamanho_figura:
            plt.figure(figsize=tamanho_figura)
        
        plt.imshow(img)
        plt.axis('off')
        
        if titulo:
            plt.title(titulo)
        
        plt.show()
        
    except Exception as e:
        print(f"Erro ao baixar ou exibir a imagem: {e}")