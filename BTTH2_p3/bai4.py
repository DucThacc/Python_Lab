"""Tệp nén là một loại lưu trữ chứa một hoặc nhiều tệp đã bị giảm kích thước.
Nén tập tin trong các hệ điều hành hiện đại thường khá đơn giản. 
Viết chương trình nén và giải nén tệp bằng Python
"""

import os
import zipfile

def compress(source_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isdir(source_path):
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    abs_path = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_path, os.path.dirname(source_path))
                    zipf.write(abs_path, rel_path)
        else:
            zipf.write(source_path, os.path.basename(source_path))
    print(f"✅ Đã nén '{source_path}' thành '{output_zip}'")

def decompress(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"✅ Đã giải nén '{zip_path}' vào '{extract_to}'")

if __name__ == "__main__":
    compress("thu_muc_can_nen", "du_lieu_nen.zip")
    decompress("du_lieu_nen.zip", "thu_muc_giai_nen")
