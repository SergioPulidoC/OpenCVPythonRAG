# src/Extraction/opencv_extractor.py

from typing import List, Optional
from langchain.document_loaders import UnstructuredURLLoader  # Example loader, adjust if using a different one

class OpenCVExtractor:
    def __init__(self, urls: List[str], output_path: Optional[str] = None):
        """
        Initialize the extractor with a list of URLs and an optional output path.
        
        Parameters:
        - urls (List[str]): List of OpenCV documentation URLs to extract.
        - output_path (str, optional): Path to save the extracted content, if required.
        """
        self.urls = urls
        self.output_path = output_path

    def extract_content(self):
        """
        Extracts content from the specified URLs using UnstructuredURLLoader.
        
        Returns:
        - extracted_data (List[str]): List of extracted text data from the URLs.
        """
        loader = UnstructuredURLLoader(urls=self.urls)
        documents = loader.load()
        extracted_data = [doc.page_content for doc in documents]
        
        if self.output_path:
            self._save_to_file(extracted_data)
        
        return extracted_data

    def _save_to_file(self, data: List[str]):
        """
        Saves extracted data to a specified output file.
        
        Parameters:
        - data (List[str]): List of extracted text data to save.
        """
        with open(self.output_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(item + '\n')
        print(f"Data saved to {self.output_path}")
