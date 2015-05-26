1. use main to get train data first 
2. convert to convert info.dat (for postive dat file)
3. use create sample
4. train cascade

cmd

opencv_traincascade.exe -data out -vec train/pos/frame_images/out_post.vec -bg train/neg/sub_images/info_neg_path.dat -numPos 1000 -numNeg 1000 -numStages 2 -mode BASIC -featureType LBP -minHitRate 0.999 -maxFalseAlarmRate 0.5
