#include <iostream>
#include <sstream>
#include <cmath>
#include <vector>
using namespace std;

// Thoughts:
// Maybe try an array of cells?
// There should be a different board class for each combo of rows/col. 

int randInt(int leng, int seed){ //returns an int from 0 to leng-1 (inclusive), use seed up to 40
    srand((unsigned) time(NULL));
    int randNum = ((int) ((pow(rand(), 2 + (seed/80) )) / (pow(10, seed%10)))) % leng;
    return randNum;
    //Def not even close to a good rand num gen, but it works
};

class board {
    public:
        vector<int> mineX;
        vector<int> mineY;
        vector<vector<int>> mineVec;
        int xRows, yCols, zMines;
        board(int xSet, int ySet, int zSet) {
            xRows = xSet;
            yCols = ySet;
            zMines = zSet;
            //setUp board 2d Vector
            vector<int> rowZeros;
            for (int i = 0; i < yCols; i++)
                rowZeros.push_back(0);
            
            for (int i = 0; i < xRows; i++)
                mineVec.push_back(rowZeros);
            }
        
        void genMines(){ //fill the mineX and mineY vectors
            int overKill = 100; //deal with repeat mines by adding 10+ slots
            for(int seed = 0; seed < zMines + overKill; seed++)
                mineX.push_back(randInt(xRows, seed));
            for(int seed = zMines; seed < 2 * (zMines + overKill); seed++)
                mineY.push_back(randInt(yCols, seed));
        }
        void putMines(){ //need to deal with repeats
            int put = 0;
            for(int i = 0; i < mineX.size(); i++){
                if(put >= zMines || mineVec[mineX[i]][mineY[i]] < 0){
                    continue;
                }
                else {
                mineVec[mineX[i]][mineY[i]] = -20;
                put++;
                }
            }
        }
        void view() {
            for(int i = 0; i < mineVec.size(); i++){
                std::cout << "\n";
                for(int j = 0; j < mineVec[j].size(); j++)
                    std::cout << mineVec[i][j] << " ";
            }
        }
};

int main(){
    board myBoard(10, 10, 9);
    myBoard.genMines();
    myBoard.putMines();
    std::cout << myBoard.mineVec.size() << " by " << myBoard.mineVec[0].size();
    myBoard.view();
    return 0;
}