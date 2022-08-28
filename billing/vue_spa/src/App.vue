<template>
  <div id="app">
    <div v-if="isLoggedIn">
      <InvoiceCreate />
    </div>
    <div v-else></div>
  </div>
</template>

<script>
import InvoiceCreate from "./components/InvoiceCreate.vue";

export default {
  name: "App",
  components: {
    InvoiceCreate,
  },
  data() {
    return {
      isLoggedIn: false,
    };
  },
  methods: {
    redirectToLogin() {
      this.isLoggedIn = false;
      window.location.href = "/auth/login/";
    },
  },
  mounted() {
    fetch("/billing/api/clients")
      .then((response) => {
        if (!response.ok && response.statusText === "Forbidden") {
          return response.json();
        }
        this.isLoggedIn = true;
      })
      .then((drfError) => {
        if (
          drfError?.detail === "Authentication credentials were not provided."
        ) {
          this.redirectToLogin();
        }
      });
  },
};
</script>

<style></style>
