#include "opencv2/opencv.hpp"

using namespace std;
using namespace cv;
Mat src;
Mat gray,edges;
int main(int argc,char **argv)
{
	Mat src= imread(argv[1],1);
	Mat gray, edges;
	cvtColor(src,gray,COLOR_BGR2GRAY);
	GaussianBlur(gray,edges,Size(5,5),1,1);
	Canny(edges,edges,0,30,3);
	imshow("gray",gray);
	imshow("edges",edges);
	imwrite("canny_edge.jpg",edges);
	waitKey(0);
}
