import CourseCard from "./CourseCard";
import schedule from BACKEND;

const times_strings = ["8:00 am", 
              "8:30 am", 
              "9:00 am", 
              "9:30 am", 
              "10:00 am", 
              "10:30 am", 
              "11:00 am", 
              "11:30 am", 
              "12:00 pm", 
              "12:30 pm", 
              "1:00 pm", 
              "1:30 pm", 
              "2:00 pm", 
              "2:30 pm", 
              "3:00 pm", 
              "3:30 pm", 
              "4:00 pm", 
              "4:30 pm", 
              "5:00 pm", 
              "5:30 pm", 
              "6:00 pm", 
              "6:30 pm", 
              "7:00 pm", 
              "7:30 pm", 
              "8:00 pm", 
              "8:30 pm", 
              "9:00 pm", 
              "9:30 pm"]

const makeDaySched = () => {
  let schedules = schedule.days;
  let code;
  let section;
  let location;
  return (
    schedules.map((day, courses) => {
      return (
    <table>
    <thead>
      <tr>
        <th>{day}</th>
      </tr>
    </thead>
    <tbody>
      {courses.map((c) => {
        code = c.code;
        section = c.section;
        location = c.location;
        CourseCard(code, section, location);
      })}
    </tbody>
  </table>
  )})
  );
}

const TimeTable = () => {
  const day_schedules = schedule.schedules;
  const times = times_strings.slice(schedule.earliest, schedule.latest + 1);
  return (
    <span>
      <table>
        <thead>
          <tr>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          {times.map((t) => {
            <tr>
              <td>t</td>
            </tr>
          })}
        </tbody>
      </table>
      {makeDaySched()};
    </span>
  );
};

export default TimeTable;
