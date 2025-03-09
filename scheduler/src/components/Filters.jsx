


const Filters = () => {
  function handleSubmit() {
    
  }

  return (
    <form id="selectors" onSubmit={handleSubmit}>
      <input
        type="text"
        name="course_code"
        pattern="[A-Z]{3, 4}\s\d{3}[A-Z]?"
        placeholder="Course Code (e.g. CPSC 110)"
        required
      />
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
      />
      <label htmlFor="end_time">End Time</label>
      <input 
      type="time" 
      name="end_time" 
      id="end_time"
      max="21:30"
      min="09:00"
      step="30"
      />
      <input type="submit"/>
    </form>
  );
};


export default Filters;