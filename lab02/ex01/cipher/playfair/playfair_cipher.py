class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key: str):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key)
        
        # Thêm các ký tự còn lại vào matrix
        for letter in remaining_letters:
            matrix.append(letter)
        if len(matrix) > 25:  # Đảm bảo độ dài của matrix không quá 25 ký tự
            matrix = matrix[:25]
        
        # Chuyển thành ma trận 5x5
        playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter: str):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text: str, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""

        # Thêm "X" vào nếu có một ký tự lẻ
        if len(plain_text) % 2 != 0:
            plain_text += "X"
        
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i + 2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:  # Hình vuông
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text: str, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:  # Hình vuông
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # Loại bỏ ký tự 'X' nếu nó là ký tự giả
        decrypted_text = decrypted_text.replace('X', '')
        
        return decrypted_text
