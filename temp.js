function weightedDistanceMatching(poseVector1, poseVector2) {
    let vector1PoseXY = poseVector1.slice(0, 34);
    let vector1Confidences = poseVector1.slice(34, 51);
    let vector1ConfidenceSum = poseVector1.slice(51, 52);
  
    let vector2PoseXY = poseVector2.slice(0, 34);
  
    // First summation
    let summation1 = 1 / vector1ConfidenceSum;
  
    // Second summation
    let summation2 = 0;
    for (let i = 0; i < vector1PoseXY.length; i++) {
      let tempConf = Math.floor(i / 2);
      let tempSum = vector1Confidences[tempConf] * Math.abs(vector1PoseXY[i] - vector2PoseXY[i]);
      summation2 = summation2 + tempSum;
    }
  
    return summation1 * summation2;
  }