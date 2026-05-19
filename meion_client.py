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
