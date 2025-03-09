import React from "react";
import { useState } from "react";

const Filters = () => {
  const [courseInputList, setCourseInput] = useState([{}]);

  function handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const body = Object.fromEntries(formData);
    fetch('http://localhost:4444/')
  }

  const handleAddCourse = () => {
    setCourseInput([...courseInputList, {}]);
  };

  const handleRemoveCourse = (index) => {
    const list = [...courseInputList];
    list.splice(index, 1);
    setCourseInput(list);
  };

  return (
    <form id="selectors" onSubmit={handleSubmit}>
      {courseInputList.map((singleCourse, index) => (
        <div>
          <input
            key={index}
            type="text"
            name="course_code"
            pattern="[A-Z]{3, 4}\s\d{3}[A-Z]?"
            placeholder="Course Code (e.g. CPSC 110)"
            required
          />
          {courseInputList.length - 1 === index &&
            courseInputList.length < 12 && (
              <button onClick={handleAddCourse}>Add course</button>
            )}
          {courseInputList.length > 1 && (
            <button onClick={() => handleRemoveCourse(index)}>Remove</button>
          )}
        </div>
      ))}
      <label htmlFor="term">Term</label>
      <select name="term" id="term">
        <option value="1">Term 1</option>
        <option value="2">Term 2</option>
        <option value="3">Full Year</option>
      </select>
      <label htmlFor="start_time">Start Time</label>
      <input
        type="time"
        name="start_time"
        id="start_time"
        max="20:30"
        min="08:00"
        step="30"
        value="08:00"
      />
      <label htmlFor="end_time">End Time</label>
      <input
        type="time"
        name="end_time"
        id="end_time"
        max="21:30"
        min="09:00"
        step="30"
        value="21:30"
      />
      <input type="submit" />
    </form>
  );
};

export default Filters;
