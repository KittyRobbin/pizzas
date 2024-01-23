import { Switch, Route } from "react-router-dom";
import Navbar from "./Navbar";
import Restaurant from "./Restaurant";
import Home from "./Home";
import RestaurantPizzaForm from "./RestaurantPizzaForm";

function App() {
  return (
    <div>
      <Navbar />
      <main>
        <Switch>
          <Route exact path="/restaurant_pizzas/new">
            <RestaurantPizzaForm />
          </Route>
          <Route exact path="/restaurants/:id">
            <Restaurant />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
        </Switch>
      </main>
    </div>
  );
}

export default App;