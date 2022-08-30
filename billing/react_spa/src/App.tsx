import React from "react";
import { gql, useMutation, useQuery } from "@apollo/client";
import Form from "./Form";
import Select from "./Select";

import "./App.css";

const GET_CLIENTS = gql`
  query getClients {
    getClients {
      id
      email
    }
  }
`;

const CREATE_INVOICE = gql`
  mutation createInvoice($invoice: InvoiceInput!) {
    createInvoice(invoice: $invoice) {
      date
      state
    }
  }
`;

const App = () => {
  const { loading, data } = useQuery(GET_CLIENTS);
  const [createInvoice, { error, loading: mutationLoading }] =
    useMutation(CREATE_INVOICE);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    await createInvoice({
      variables: {
        invoice: {
          user: 1,
          date: "2021-05-01",
          dueDate: "2021-05-31",
          state: "UNPAID",
          items: [
            {
              description: "Django consulting",
              price: 7000,
              taxed: true,
              quantity: 1,
            },
          ],
        },
      },
    });
  };

  return loading ? (
    <p>Loading ...</p>
  ) : (
    <div className="App">
      <Form handleSubmit={handleSubmit}>
        <Select id="user" name="user" options={data.getClients}></Select>
        <div>
          <label htmlFor="dueDate">Due Date</label>
          <input type="date" id="dueDate" name="dueDate" required />
        </div>
        <div>
          <label htmlFor="quantity">Qty</label>
          <input
            type="number"
            id="quantity"
            name="quantity"
            min={0}
            max={10}
            required
          />
        </div>
        <div>
          <label htmlFor="price">Price</label>
          <input
            type="number"
            id="price"
            name="price"
            min={0}
            step={0.01}
            required
          />
        </div>
        <div>
          <label htmlFor="taxed">Taxed</label>
          <input type="checkbox" id="taxed" name="taxed" />
        </div>
        {mutationLoading ? (
          <p>Creating the invoice...</p>
        ) : (
          <button type="submit">CREATE INVOICE</button>
        )}
      </Form>
    </div>
  );
};

export default App;
