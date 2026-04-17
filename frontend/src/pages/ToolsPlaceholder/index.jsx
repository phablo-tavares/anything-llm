import React from "react";
import PasswordModal, { usePasswordModal } from "@/components/Modals/Password";
import { FullScreenLoader } from "@/components/Preloader";
import { isMobile } from "react-device-detect";
import Sidebar, { SidebarMobileHeader } from "@/components/Sidebar";

export default function ToolsPlaceholder() {
  const { loading, requiresAuth, mode } = usePasswordModal();

  if (loading) return <FullScreenLoader />;
  if (requiresAuth !== false)
    return <>{requiresAuth !== null && <PasswordModal mode={mode} />}</>;

  return (
    <div className="w-screen h-screen overflow-hidden bg-zinc-950 light:bg-slate-50 flex">
      {!isMobile ? <Sidebar /> : <SidebarMobileHeader />}
      <div className="flex flex-col flex-1 h-full w-full">
        <iframe
          src="https://rennovarfm.lovable.app/"
          className="w-full h-full border-0"
          title="Matriz RFM"
        />
      </div>
    </div>
  );
}
