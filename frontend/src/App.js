import { useEffect, useState } from "react";

function App() {

  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    const loadData = () => {
      fetch('http://localhost:8000/api/customers/')
      .then(response => response.json())
      .then(data => setCustomers(data))
    }
    loadData();
  }, []);

  return (
    <div className="App">
      {customers.map(customer => (
        <h1 key={customer.id}>{customer.first_name} {customer.last_name}</h1>
      ))}
    </div>
  );
}

export default App;
