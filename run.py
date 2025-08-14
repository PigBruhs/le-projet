class image_processor:
    def __init__(self):
        self.model_version = 2.3

    def process_image(self, image_file) -> dict:
        """Process the uploaded image and detect disease.

        Args:
            image_file: The uploaded image file

        Returns:
            Dict containing detection results
        """
        # This is a mock implementation
        # In a real application, you would implement your disease detection logic here

        # Example return data
        return {
            "disease_type": "稻瘟病",
            "confidence": 0.95,
            "bbox": {
                "x1": 100,
                "y1": 100,
                "x2": 300,
                "y2": 300
            },
            "area": 40000,
            "severity": "中度",
            "suggestion": {
                "immediate": "摘除病叶，喷洒三环唑",
                "long_term": "定期巡检，加强通风"
            },
            "model_version": self.model_version,
        }