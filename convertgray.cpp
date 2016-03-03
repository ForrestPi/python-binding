#include <iostream>

using namespace std;
#include<cv.h>   //cv.h OpenCV的主要功能头文件，务必要；
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
using namespace cv;
int main(int argc, char*argv[])
{
    //获取图像
    if (argc!=3)
    {
        cout << "参数个数错误！"<<endl;
        return -1;
    }
    cv::Mat mat1 = cv::imread(argv[1],1);
    if(!mat1.data)
    {
            std::cout<<"Cannot Load File!"<<std::endl;
            return -1;
    }
    if(mat1.channels()!=3)
    {
        std::cout<<argv[1]<<"已经是单通道图像"<<endl;
    }
    cv::Mat mat2;
    cvtColor(mat1,mat2,CV_RGB2GRAY);
    cv::imwrite(argv[2],mat2);

    return 0;
}
