#include <iostream>
#include <sstream>
#include <cmath>
#include <vector>
using namespace std;

int randInt(int leng, int seed){ //returns an int from 0 to leng-1 (inclusive), use seed up to 40
    srand((unsigned) time(NULL));
    int randNum = ((int) ((pow(rand(), 2 + (seed/40) )) / (pow(10, seed%10)))) % leng;
    return randNum;
    //Def not even close to a good rand num gen, but it works
};

class board {
    public:
        vector<int> mineX;
        vector<int> mineY;
        int xRows, yCols, zMines;
        board(int xSet, int ySet, int zSet) {
            xRows = xSet;
            yCols = ySet;
            zMines = zSet;
        }
        void genMines(){ //fill the mineX and mineY vectors
            for(int seed = 0; seed < zMines; seed++)
                mineX.push_back(randInt(xRows, seed));
            for(int seed = zMines; seed < 2 * zMines; seed++)
                mineY.push_back(randInt(yCols, seed));
        }

};
int main(){
    board myBoard(10, 10, 8);
    myBoard.genMines();
    //std::cout << *myBoard.mineX.cbegin() << "\n";
    std::cout << myBoard.mineX.at(7);
    return 0;
}