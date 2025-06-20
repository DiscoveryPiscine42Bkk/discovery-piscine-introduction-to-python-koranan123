def checkmate(board_str):
    board = [list(row) for row in board_str.strip().split('\n')]#แปลงข้อความเป็นตาราง
    size = len(board)#กำหนดขอบเขตloop

    king_pos = None#หา k 
    for y in range(size):
        for x in range(size):
            if board[y][x] == 'K':
                king_pos = (y, x)
                break
        if king_pos:
            break #ถ้าเจอkที่ตำแหน่ง k จะหยุดทำงาน

    if not king_pos:
        return#ถ้าไม่เจอ จะไม่ตรวจ

    yk, xk = king_pos #แยกคิง

    def in_bounds(y, x):#ฟังชันก์ที่ใช้ตรวจสอบขนาดของกระดาน
        return 0 <= y < size and 0 <= x < size

    def check_pawn():ตรวจสอบว่าตัวไหนจะกินkได้
        for dy, dx in [(1, -1), (1, 1)]:
            ny, nx = yk + dy, xk + dx
            if in_bounds(ny, nx) and board[ny][nx] == 'P':
                return True
        return False

    def check_line(directions, targets): #ตรวจสอบการโจมโดนคิงว่าโดนมั้ย 
        for dy, dx in directions:
            ny, nx = yk + dy, xk + dx
            while in_bounds(ny, nx):
                cell = board[ny][nx]
                if cell == '.':
                    ny += dy
                    nx += dx
                    continue #การทำงานของทิศทาง เช่นการเดินตรง เฉียง
                elif cell in targets:
                    return True
                else:
                    break
        return False

    def check_rook():#บวก
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return check_line(directions, ['R'])

    def check_bishop():
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return check_line(directions, ['B'])

    def check_queen():
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        return check_line(directions, ['Q'])

    if check_pawn() or check_rook() or check_bishop() or check_queen():
        print("Success")
    else:
        print("Fail")
