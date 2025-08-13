import whisper
import tempfile
import os
import traceback
import ffmpeg

#load Whisper model
    # Lưu ý: Bạn cần cài đặt thư viện Whisper trước khi sử dụng.
print("Loading Whisper model...")
whisper_model = whisper.load_model("medium")
print("Whisper model loaded.")
    
    
#==============================HÀM CHUẨN HÓA ÂM THANH==============================
# Hàm này sẽ chuẩn hóa file âm thanh làm đầu vào cho các mô hình nhận âm thanh như Whisper và các mô hình khác.

def normalize_audio_for_transcription(input_path, output_path):
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path,
                    ac=1,          # mono
                    ar=16000,      # 16000 Hz
                    sample_fmt='s16')  # 16-bit PCM
            .overwrite_output()
            .run(quiet=True)
        )
        print(f"✅ Chuẩn hóa thành công, lưu tại: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Lỗi khi chuẩn hóa bằng ffmpeg: {e}")
        return False

#==============================TRANSCRIPTION FUNCTION VỚI WHISPER==============================

def transcribe_audio_with_whisper(audio_file, language="vi"):
    """
    Hàm này nhận một file audio được upload, thực hiện tiền xử lý (chuẩn hóa)
    rồi mới tiến hành phiên âm để tăng độ chính xác.
    """
    temp_input_path = None
    temp_normalized_path = None
    
    try:
        # --- Bước 1: Lưu file upload gốc vào một file tạm ---
        # Lấy đuôi file gốc để pydub có thể nhận dạng đúng
        original_suffix = os.path.splitext(audio_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=original_suffix) as temp_in_file:
            for chunk in audio_file.chunks():
                temp_in_file.write(chunk)
            temp_input_path = temp_in_file.name

        # --- Bước 2: Tạo một đường dẫn tạm cho file đã được chuẩn hóa ---
        with tempfile.NamedTemporaryFile(delete=False, suffix="_normalized.wav") as temp_out_file:
            temp_normalized_path = temp_out_file.name
            
        # --- Bước 3: Gọi hàm xử lý âm thanh ---
        # Hàm này sẽ đọc từ file tạm (A) và ghi ra file tạm (B)
        success = normalize_audio_for_transcription(
            input_path=temp_input_path,
            output_path=temp_normalized_path
        )

        if not success:
            # Nếu chuẩn hóa thất bại, trả về lỗi
            return "Đã xảy ra lỗi trong quá trình chuẩn hóa file âm thanh."

        # --- Bước 4: Phiên âm file ĐÃ ĐƯỢC CHUẨN HÓA (file B) ---
        print(f"🎤 Bắt đầu phiên âm file đã được xử lý...")
        result = whisper_model.transcribe(temp_normalized_path, language=language, fp16=False)
        
        return result.get("text", "Không thể chuyển đổi văn bản.")

    except Exception as e:
        print(f"❌ Lỗi tổng thể trong quá trình phiên âm: {e}")
        traceback.print_exc()
        return "Đã xảy ra lỗi trong quá trình xử lý file âm thanh."

    finally:
        # --- Bước 5: Dọn dẹp cả hai file tạm ---
        # Luôn đảm bảo file tạm được xóa dù có lỗi hay không
        if temp_input_path and os.path.exists(temp_input_path):
            os.remove(temp_input_path)
            print(f"🚮 Đã xóa file tạm gốc: {os.path.basename(temp_input_path)}")
        if temp_normalized_path and os.path.exists(temp_normalized_path):
            os.remove(temp_normalized_path)
            print(f"🚮 Đã xóa file tạm đã chuẩn hóa: {os.path.basename(temp_normalized_path)}")