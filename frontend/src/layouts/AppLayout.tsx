import Sidebar from "../components/Sidebar";

function AppLayout() {
  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <main className="flex-1 p-4">
        <h4>Main Content</h4>
      </main>
    </div>
  );
}

export default AppLayout;
