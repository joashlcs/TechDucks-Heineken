<template>
  <div class="d-flex flex-column align-items-center justify-content-center" style="height: 100vh;">
    <div class="logo">
      <img class="fit-picture" src="../assets/heineken.png"/>
    </div>
    <div v-if="result === 'passed'" class="text-center mt-1">
      <b>
        <h2>Congratulations,</h2>
        <h2>You're under 0.600s again!</h2>
      </b>
      <img class="gif" src="../assets/consecutivebeer.png" alt="Looping GIF" loop>
      <div class="m-3 mb-4 text-center">
        <div class="button-container">
          <button class="btn-heineken-page background-heineken-green" @click="drinkaid">TRY DRINKAID FOR FREE</button>
          <span class="vertical-center"><b>OR</b></span>
          <button class="btn-heineken-second-option" @click="checkout">GET NEXT CUP @ {{ percentageOff }}% OFF</button>
        </div>
      </div>
    </div>
    <div v-else class="text-center mt-1">
      <b>
        <h2>Oh no, You're over 0.600s!</h2>
      </b>
      <img class="gif" src="../assets/warningcrash.png" alt="Car Crash Warning">
      <b>
        <h2 class="m-0">Don't Drive, Get DrinkAid</h2>
      </b>
      <div class="m-4 text-center">
        <div class="button-container">
          <button class="btn-heineken-page background-heineken-green" @click="drinkaid">TRY DRINKAID FOR 30% OFF</button>
          <span class="vertical-center"><b>OR</b></span>
          <button class="btn-heineken-third-option" @click="cancelButton">No Thanks</button>
        </div>
      </div>
    </div>
    <div class="text-center mt-4">
      <p>*Psst... DrinkAid helps prevent hangovers!</p>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import QRCodeScanner from "@/components/QRCodeScanner.vue";

export default {
  name: 'LandingPage',
  data() {
    return {
      msg: '',
      userid: null,
      result: null,
      timeLeft: 15,
      percentageOff: 0,
      final_decision: null,
      product: "beer"
    };
  },
  components: {
    QRCodeScanner
  },
  created() {
    const resultData = this.$route.params;
    this.userid = resultData.id;
    this.result = resultData.result;
    console.log(`User ID: ${this.userid}`);
    console.log(`User ID: ${this.result}`);
    this.getPercentageOff();
  },
  methods: {
    cancelButttonAPI() {
      if (this.userid === null) {
        console.log("Missing user_id");
        return Promise.reject("Missing user_id");
      }

      const payload = {
        document_id: this.userid,
        button_id: "normal_beer_button",
        read: true
      };
      const path = `http://127.0.0.1:5000/${this.userid}/check-out-false`; // Call API to update final buying decision of drinkaid after consecutive failing

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          return response;
        })
        .catch((error) => {
          console.log(error);
          throw error;
        });
    },
    cancelButton() {
      this.final_decision = false;
      this.cancelButttonAPI()
        .then((response) => {
          console.log("Rejected discounted Drinkaid")
          this.$router.push('/');
        })
        .catch((error) => {
          console.log(error)
        });
    },
    drinkaid() {
      if (this.result === 'passed') {
        this.freeDrinkAidAPI()
        console.log("Free Drink Aid Logged")
        this.$router.push(`/checkout/drinkaid/${this.userid}/free`)
      } else {
        this.discountedDrinkAidAPI()
        console.log("Discounted Drink Aid Logged")
        this.$router.push(`/checkout/drinkaid/${this.userid}/discounted`)
      }
    },
    checkout() {
      this.discountedBeerAPI()
      console.log("Discounted Beer Logged")
      this.$router.push(`/checkout/beer/${this.userid}/discounted`)
    },
    startCountdown() {
      setInterval(() => {
        if (this.timeLeft > 0) {
          this.timeLeft--;
        } else {
          this.goToLandingPage();
        }
      }, 1000);
    },
    getPercentageOff() {
      this.getBeerPercentageOff()
        .then((response) => {
          const data = response.data;
          this.percentageOff = data.discount_percentage;
          console.log(this.percentageOff)
        })
        .catch((error) => {
          console.log(error);
        })
    },
    getBeerPercentageOff() {
      if (this.userid === '') {
        console.log("Missing document_id");
        return Promise.reject("Missing document_id");
      }

      const payload_landing = {
        document_id: this.userid,
        read: true
      };
      const path = `http://127.0.0.1:5000/${this.userid}/discount`;

      return axios.post(path, payload_landing, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          return response;
        })
        .catch((error) => {
          console.log(error);
          throw error;
        });
    },
    freeDrinkAidAPI() {
      if (this.userid === null) {
        console.log("Missing userid");
        return Promise.reject("Missing userid");
      }

      const payload = {
        document_id: this.userid,
        button_id: "free_drinkaid_button",
        read: true
      };
      const path = `http://127.0.0.1:5000/checkout/${this.userid}`; // Call API to update final buying decision of drinkaid after consecutive failing

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          return response;
        })
        .catch((error) => {
          console.log(error);
          throw error;
        });
    },
    discountedDrinkAidAPI() {
      if (this.user_id === null) {
        console.log("Missing userid");
        return Promise.reject("Missing userid");
      }

      const payload = {
        document_id: this.userid,
        button_id: "discount_drinkaid_button",
        read: true
      };
      const path = `http://127.0.0.1:5000/${this.userid}/check-out-false`; // Call API to update final buying decision of drinkaid after consecutive failing

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          return response;
        })
        .catch((error) => {
          console.log(error);
          throw error;
        });
    },
    discountedBeerAPI() {
      if (this.userid === null) {
        console.log("Missing userid");
        return Promise.reject("Missing userid");
      }

      const payload = {
        document_id: this.userid,
        button_id: "discount_beer_button",
        read: true
      };
      const path = `http://127.0.0.1:5000/checkout/${this.userid}`; // Call API to update final buying decision of drinkaid after consecutive failing

      return axios.post(path, payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => {
          return response;
        })
        .catch((error) => {
          console.log(error);
          throw error;
        });
    },
  },
};
</script>

<style>
h1 {
  line-height: 1 !important;
}
.gif {
  max-width: 300px;
  max-height: 300px;
}

.gif big{
  max-width: 400px;
  max-height: 400px;
}

.fit-picture {
  width: 250px;
}

.btn-heineken-page {
  transform: scale(0.9) !important;
  font-size: 1rem !important;
  max-width: 150px;
  border-radius: 15px;
  padding: 10px;
}

.btn-heineken-second-option {
  transform: scale(0.9) !important;
  font-size: 1rem !important;
  max-width: 150px;
  background-color: transparent;
  border: none;
  padding: 13px;
  color: black;
  box-shadow: 0 0 0 4px #038135 inset;
  border-radius: 15px;
}

.btn-heineken-third-option {
  transform: scale(0.9) !important;
  font-size: 1rem !important;
  max-width: 150px;
  background-color: transparent;
  border: none;
  padding: 25px 35px;
  color: black;
  box-shadow: 0 0 0 4px #E30613 inset;
  border-radius: 15px;
}

.background-heineken-green {
  background-color: #038135 !important;
  color: white !important;
}

.background-heineken-red {
  background-color: #E30613 !important;
  color: white !important;
}

.button-container {
  display: flex;
  align-items: center;
  justify-content: center;
  transform: scale(1.2);
  margin-top: 25px;
}

.vertical-center {
  margin: 0 10px;
}

</style>
