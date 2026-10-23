import Sidebar from "./components/Sidebar";

function App() {
  return (
    <div className="flex">
      <Sidebar />
      <main className="flex-1 p-4">
        <h1 className="text-3xl font-bold text-blue-500">Main Content</h1>
      </main>
    </div>
  );
}

export default App;
