import { Link } from "react-router-dom";

function Navbar() {
  return (
    <header>
      <h1>
        <Link to="/">Restaurant Pizzas</Link>
      </h1>
    </header>
  );
}

export default Navbar;