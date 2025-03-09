import React from "react";

const CourseCard = ({ CourseCode, section, location }) => {
  return (
    <div>
      <div>
        <p>{CourseCode}</p>
        <p>{section}</p>
      </div>
      <p>(concat("@ ", {location}))</p>
    </div>
  );
};

export default CourseCard;
