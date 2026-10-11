import base64
import cv2
import numpy as np


def frame_to_base64(frame: np.ndarray, quality: int = 70) -> str:
    """
    OpenCV frame (numpy array) ko base64 string mein convert karta hai.
    Quality 70 — chhota payload, analysis ke liye kaafi.
    """
    # Frame ko RGB mein convert karo (Streamlit RGB deta hai)
    if len(frame.shape) == 3 and frame.shape[2] == 3:
        # Already RGB
        pass
    
    # Resize karo — chhota payload
    h, w = frame.shape[:2]
    if w > 640:
        scale = 640 / w
        frame = cv2.resize(frame, (640, int(h * scale)))
    
    # JPEG encode
    _, buffer = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, quality])
    b64 = base64.b64encode(buffer).decode("utf-8")
    return b64


def overlay_face_info(frame: np.ndarray, face_data: dict) -> np.ndarray:
    """
    Frame pe face info overlay karta hai.
    face_data = response from /analyze_frame
    """
    frame = frame.copy()
    
    if not face_data.get("face_detected"):
        cv2.putText(
            frame, "No face detected",
            (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
        )
        return frame
    
    if face_data.get("face_count", 0) > 1:
        cv2.putText(
            frame, f"{face_data['face_count']} faces!",
            (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2,
        )
        return frame
    
    # Single face — info overlay
    emotion = face_data.get("emotion", "?")
    attention = face_data.get("attention_score", 0)
    
    # Emotion color code
    color_map = {
        "happy": (0, 255, 0),
        "neutral": (200, 200, 200),
        "sad": (255, 100, 0),
        "angry": (0, 0, 255),
        "fear": (0, 165, 255),
        "surprise": (255, 255, 0),
    }
    color = color_map.get(emotion, (255, 255, 255))
    
    cv2.putText(
        frame, f"Emotion: {emotion}",
        (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
    )
    cv2.putText(
        frame, f"Attention: {attention:.1f}/10",
        (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
    )
    
    if face_data.get("warning"):
        cv2.putText(
            frame, face_data["warning"],
            (20, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (0, 0, 255), 2,
        )
    
    return frame