import requests
from config import API_URL, API_TIMEOUT


class InterviewAPI:
    """Wrapper class for AI Interviewer API."""
    
    def __init__(self, base_url: str = API_URL):
        self.base_url = base_url
    
    def health_check(self) -> bool:
        try:
            r = requests.get(f"{self.base_url}/", timeout=3)
            return r.status_code == 200
        except Exception:
            return False
    
    def upload_resume(self, file) -> dict:
        """Upload PDF resume, return extracted text."""
        files = {"file": (file.name, file.getvalue(), "application/pdf")}
        r = requests.post(
            f"{self.base_url}/upload_resume",
            files=files,
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    
    def start_interview(self, resume_text: str, job_description: str) -> dict:
        """Start new interview session."""
        r = requests.post(
            f"{self.base_url}/start_interview",
            json={"resume_text": resume_text, "job_description": job_description},
            timeout=API_TIMEOUT,
        )
        r.raise_for_status()
        return r.json()
    
    def submit_answer(self, session_id: str, answer: str) -> dict:
        """Submit answer, get next question or feedback."""
        r = requests.post(
            f"{self.base_url}/submit_answer",
            json={"session_id": session_id, "answer": answer},
            timeout=API_TIMEOUT,
        )
        r.raise_for_status()
        return r.json()
    
    def get_session(self, session_id: str) -> dict:
        """Get session status."""
        r = requests.get(
            f"{self.base_url}/session/{session_id}",
            timeout=10,
        )
        r.raise_for_status()
        return r.json()


    def analyze_frame(self, session_id: str, image_base64: str) -> dict:
        """Analyze video frame for facial expressions."""
        r = requests.post(
            f"{self.base_url}/analyze_frame",
            json={"session_id": session_id, "image_base64": image_base64},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()

    def transcribe_audio(self, audio_bytes: bytes, filename: str = "audio.webm") -> str:
        """Audio bhejo, text lo."""
        files = {"file": (filename, audio_bytes, "audio/webm")}
        r = requests.post(
            f"{self.base_url}/transcribe",
            files=files,
            timeout=60,
        )
        r.raise_for_status()
        return r.json()["text"]
