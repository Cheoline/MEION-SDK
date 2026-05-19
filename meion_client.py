# -*- coding: utf-8 -*-
import os
import requests

class MeionClient:
    """
    Cliente oficial en Python para conectar tus Agentes de IA, Chatbots
    y asistentes cognitivos a la base de memoria persistente MEION.
    """
    
    def __init__(self, api_key=None, server_url=None):
        """
        Inicializa el cliente cargando las llaves desde las variables de entorno
        o mediante argumentos directos.
        """
        # Intentar cargar desde las variables de entorno o usar los argumentos
        self.api_key = api_key or os.environ.get("MEION_API_KEY")
        self.server_url = server_url or os.environ.get("MEION_SERVER_URL") or "https://meionia.com"
        
        # Sanitizar URL del servidor
        if not self.server_url.startswith("http://") and not self.server_url.startswith("https://"):
            self.server_url = "https://" + self.server_url
        if self.server_url.endswith("/"):
            self.server_url = self.server_url[:-1]
            
        if not self.api_key:
            raise ValueError(
                "❌ Error: Se requiere una API Key de MEION. "
                "Cárgala como variable de entorno MEION_API_KEY o pásala al inicializar el cliente."
            )

    def _get_headers(self):
        return {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def memorize(self, text):
        """
        Guarda un recuerdo en el núcleo de memoria persistente de MEION.
        
        :param text: El pensamiento, hecho, conversación o documento a memorizar.
        :return: Diccionario con estadísticas de compresión y confirmación.
        """
        if not text or not text.strip():
            raise ValueError("El texto a memorizar no puede estar vacío.")
            
        url = f"{self.server_url}/api/memorize"
        payload = {"texto": text}
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"Fallo al conectar con el servidor de memoria: {e}"
            }

    def search(self, query, format_ai=False, desde=None, hasta=None):
        """
        Realiza una búsqueda semántica de recuerdos relevantes para proveer contexto a tu IA.
        
        :param query: El criterio o pregunta de búsqueda.
        :param format_ai: Si es True, retorna el contexto formateado listo para inyectar a tu LLM (Gemma, GPT, Claude).
        :param desde: Filtro de fecha de inicio (formato YYYY-MM-DD).
        :param hasta: Filtro de fecha de fin (formato YYYY-MM-DD).
        :return: Lista de recuerdos relevantes o diccionario formateado para IA.
        """
        url = f"{self.server_url}/api/search"
        params = {"q": query}
        
        if format_ai:
            params["format"] = "ai"
        if desde:
            params["desde"] = desde
        if hasta:
            params["hasta"] = hasta
            
        try:
            response = requests.get(url, params=params, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"Fallo al buscar recuerdos: {e}"
            }

    def get_stats(self):
        """
        Obtiene las métricas de rendimiento del cerebro digital del usuario.
        """
        url = f"{self.server_url}/api/stats"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"Fallo al recuperar métricas: {e}"
            }

    def delete_memory(self, uuid):
        """
        Elimina un recuerdo del cerebro molecular mediante su UUID único.
        
        :param uuid: El identificador único del recuerdo a eliminar.
        :return: Diccionario con el resultado de la eliminación.
        """
        if not uuid:
            raise ValueError("El UUID del recuerdo a eliminar no puede estar vacío.")
            
        url = f"{self.server_url}/api/memory/delete"
        payload = {"uuid": uuid}
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"Fallo al eliminar recuerdo: {e}"
            }

    def upload_image(self, file_path):
        """
        Sube una imagen al servidor de MEION para ser procesada y comprimida cromáticamente a formato .itom.
        
        :param file_path: Ruta local del archivo de imagen (PNG, JPG, JPEG, etc.).
        :return: Diccionario con el resultado de la compresión cromática, incluyendo el nombre de archivo .itom generado.
        """
        if not file_path or not os.path.exists(file_path):
            raise FileNotFoundError(f"No se pudo encontrar el archivo de imagen especificado: {file_path}")
            
        url = f"{self.server_url}/api/itom/compress"
        headers = {
            "X-API-Key": self.api_key
        }
        
        try:
            with open(file_path, 'rb') as f:
                files = {'file': (os.path.basename(file_path), f)}
                response = requests.post(url, files=files, headers=headers)
                response.raise_for_status()
                return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"Fallo al subir y comprimir imagen cromática: {e}"
            }

    def download_image(self, filename, output_path):
        """
        Descarga una imagen (comprimida .itom o reconstruida .png) desde el servidor de MEION.
        
        :param filename: El nombre de archivo en el servidor (ej: 'decompressed_abc.png' o 'abc.itom').
        :param output_path: Ruta local donde se guardará el archivo descargado.
        :return: True si la descarga fue exitosa, o un diccionario con el error.
        """
        if not filename:
            raise ValueError("El nombre del archivo a descargar no puede estar vacío.")
            
        url = f"{self.server_url}/api/itom/download/{filename}"
        params = {"api_key": self.api_key}
        
        try:
            response = requests.get(url, params=params, stream=True)
            response.raise_for_status()
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"Fallo al descargar archivo: {e}"
            }
