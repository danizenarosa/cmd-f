import "./App.css";
import Filters from "./components/Filters";
import TimeTable from "./components/TimeTable";

class App extends React.Component {
  render() {
    return (
      <body>
        <Filters />
        <TimeTable />
      </body>
    );
  }
}

export default App;
