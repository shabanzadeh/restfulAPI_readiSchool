import { defineConfig } from 'vite'
import reactRefresh from "@vitejs/plugin-react-refresh";


//vitejs.dev/config/
export default defineConfig({
  server: {
    port: 4000,
  },
  plugins: [reactRefresh()],
});
