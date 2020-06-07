#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

int main() {
	cv::namedWindow("vid", cv::WINDOW_AUTOSIZE);
	cv::VideoCapture cap;
	cap.open("../../resources/trump.mp4");
	cv::Mat frame;
	for (;;) {
		cap >> frame;
		if (frame.empty()) break;
		cv::imshow("vid", frame);
		
		//wait 33ms so that the vid look normal
		if (cv::waitKey(33) >= 0) break;
	}
}