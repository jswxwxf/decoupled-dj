import React from "react";

type Props = {
  children: React.ReactNode;
  handleSubmit(event: React.FormEvent<HTMLFormElement>): void;
};

const Form = ({ children, handleSubmit }: Props) => (
  <form onSubmit={handleSubmit}>{children}</form>
);

export default Form;
