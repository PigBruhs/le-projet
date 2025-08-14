from flask import Flask, request, jsonify
import time
import os
from typing import Dict, Any, Tuple
from run import image_processor


class DiseaseDetectionServer:
    def __init__(self, host: str = '127.0.0.1', port: int = 6050, model_version: str = 'v2.3'):
        """Initialize the disease detection server.

        Args:
            host: Host address to bind the server
            port: Port number to listen on
            model_version: Version of the detection model
        """
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.model_version = model_version

        # Register routes
        self.register_routes()

    def register_routes(self):
        """Register API endpoints."""
        self.app.route('/api/detect', methods=['POST'])(self.detect_disease)

    def detect_disease(self):
        """Handle disease detection requests from frontend."""
        start_time = time.time()

        try:
            # In a real application, you would:
            # 1. Get image data from request
            # 2. Process the image with your model
            # 3. Return the detection results

            # Mock detection result for demonstration
            detection_result = self._process_image(request.files.get('image'))

            process_time = int((time.time() - start_time) * 1000)  # Convert to milliseconds

            return self._create_response(
                code=0,
                msg="识别成功",
                data={
                    **detection_result,
                    "process_time": process_time
                }
            )

        except Exception as e:
            return self._create_response(
                code=1,
                msg=f"识别失败: {str(e)}",
                data=None
            )

    def _process_image(self, img) -> Dict[str, Any]:
        """Process the uploaded image and detect disease.

        Args:
            image_file: The uploaded image file

        Returns:
            Dict containing detection results
        """
        # This is a mock implementation
        # In a real application, you would implement your disease detection logic here

        # Example return data
        return image_processor.process_image(image_file=img)


    def _create_response(self, code: int, msg: str, data: Dict = None) -> Tuple[Dict[str, Any], int]:
        """Create a standardized API response.

        Args:
            code: Response code (0 for success)
            msg: Response message
            data: Response data

        Returns:
            JSON response with appropriate HTTP status
        """
        response = {
            "code": code,
            "msg": msg,
            "data": data
        }

        http_status = 200 if code == 0 else 400
        return jsonify(response), http_status

    def run(self):
        """Start the Flask server."""
        self.app.run(host=self.host, port=self.port)


if __name__ == "__main__":
    server = DiseaseDetectionServer()
    server.run()