#include <iostream>
using namespace std;
//errors line 26

class cell{
    public:
        int x;
        int y;
        bool revealed = false;
        bool hasMine = false;
        cell() { }//keep
        cell(int xIn, int yIn){
            x = xIn;
            y = yIn;
        }
};
class boardSmall{
    public:
        cell* board = new cell[10][10];
        boardSmall(){
            setUp();
        };

        void setUp(){
            for (int i = 0; i < 10; i++) {
                for (int j = 0; i < 10; j++) {
                    std::cout << i << " " << j << " " << cell(i,j).x;
                    board[i][j] = cell(i, j);

                }
            }
        }
};


int main(){
    boardSmall myBoard;
    std::cout << myBoard.board[0][0].hasMine;
    return 0;
}